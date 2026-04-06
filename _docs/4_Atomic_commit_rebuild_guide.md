# Atomic Commit Rebuild Guide (26 commits)

Цель: вручную пересобрать репозиторий с нуля так, чтобы история выглядела инженерно-правдоподобно: маленькие, независимые коммиты, каждый про одну идею.

## 0) Старт (один раз)
```bash
mkdir pizza-clean && cd pizza-clean
git init
mkdir -p backend frontend infra _docs _dev_diaries
```

Ниже: `26` атомарных коммитов с командами и точечными сниппетами.

---

## Commit 01
**Message**: `chore(repo): bootstrap folders and root readme`

```bash
git add README.md _docs/1_Описание\ структуры\ репозитория.md _docs/2_Настройка\ инструментов\ разработки.md
git commit -m "chore(repo): bootstrap folders and root readme"
```

**Snippet (`README.md`)**
```md
Оглавление
----------
1. [Описание структуры репозитория](_docs/1_Описание%20структуры%20репозитория.md)
2. [Настройка инструментов разработки](_docs/2_Настройка%20инструментов%20разработки.md)
```

## Commit 02
**Message**: `build(make): add docker compose shortcuts`

```bash
git add Makefile
git commit -m "build(make): add docker compose shortcuts"
```

**Snippet (`Makefile`)**
```make
DOCKER_COMPOSE = docker-compose -f ./infra/compose-local.yml

up:
	${DOCKER_COMPOSE} up -d --remove-orphans

down:
	${DOCKER_COMPOSE} down
```

## Commit 03
**Message**: `infra(compose): add local frontend/backend/postgres stack`

```bash
git add infra/compose-local.yml
git commit -m "infra(compose): add local frontend/backend/postgres stack"
```

**Snippet (`infra/compose-local.yml`)**
```yml
services:
  frontend:
    ports: ["8888:8888"]
  backend:
    depends_on:
      database:
        condition: service_healthy
  database:
    image: postgres:14
```

## Commit 04
**Message**: `feat(backend): add Python deps and docker image`

```bash
git add backend/requirements.txt backend/Dockerfile
git commit -m "feat(backend): add Python deps and docker image"
```

**Snippet (`backend/requirements.txt`)**
```txt
fastapi~=0.111.0
SQLAlchemy~=2.0.30
alembic~=1.13.1
asyncpg~=0.29.0
```

## Commit 05
**Message**: `feat(config): add app settings and database url`

```bash
git add backend/core/config.py backend/core/__init__.py
git commit -m "feat(config): add app settings and database url"
```

**Snippet (`backend/core/config.py`)**
```py
class Settings(BaseSettings):
    PROJECT_NAME: str = "pizza"
    POSTGRES_SERVER: str = "localhost"

    @computed_field
    @property
    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
```

## Commit 06
**Message**: `feat(db): initialize async engine and declarative base`

```bash
git add backend/db/base.py backend/db/__init__.py
git commit -m "feat(db): initialize async engine and declarative base"
```

**Snippet (`backend/db/base.py`)**
```py
engine = create_async_engine(settings.get_db_url, pool_pre_ping=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
```

## Commit 07
**Message**: `feat(db-models): add product and order entities`

```bash
git add backend/db/models.py
git commit -m "feat(db-models): add product and order entities"
```

**Snippet (`backend/db/models.py`)**
```py
class Product(Base):
    __tablename__ = 'products'
    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
```

## Commit 08
**Message**: `feat(db-models): add orders_listing cart and customer entities`

```bash
git add backend/db/models.py
git commit -m "feat(db-models): add orders_listing cart and customer entities"
```

**Snippet (`backend/db/models.py`)**
```py
class OrdersListing(Base):
    __tablename__ = 'orders_listing'

class Cart(Base):
    __tablename__ = 'carts'

class Customer(Base):
    __tablename__ = 'customers'
```

## Commit 09
**Message**: `feat(dao): add generic async DAO base`

```bash
git add backend/dao/base.py backend/dao/__init__.py
git commit -m "feat(dao): add generic async DAO base"
```

**Snippet (`backend/dao/base.py`)**
```py
class BaseDAO:
    @classmethod
    async def get_one_or_none(cls, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
```

## Commit 10
**Message**: `feat(dao): implement entity DAOs for product cart order customer`

```bash
git add backend/dao/product.py backend/dao/cart.py backend/dao/order.py backend/dao/customer.py
git commit -m "feat(dao): implement entity DAOs for product cart order customer"
```

**Snippet (`backend/dao/product.py`)**
```py
class ProductDAO(BaseDAO):
    model = Product
```

## Commit 11
**Message**: `feat(api-schema): add product schemas`

```bash
git add backend/api/schemas/product.py backend/api/schemas/__init__.py
git commit -m "feat(api-schema): add product schemas"
```

**Snippet (`backend/api/schemas/product.py`)**
```py
class SProduct(BaseModel):
    product_id: uuid.UUID
    product_title: str
```

## Commit 12
**Message**: `feat(api-schema): add order schemas`

```bash
git add backend/api/schemas/order.py
git commit -m "feat(api-schema): add order schemas"
```

**Snippet**
```py
class SOrder(BaseModel):
    customer_id: uuid.UUID
    products: List[SOrderValues]
```

## Commit 13
**Message**: `feat(api-schema): add cart and customer schemas`

```bash
git add backend/api/schemas/cart.py backend/api/schemas/customer.py
git commit -m "feat(api-schema): add cart and customer schemas"
```

**Snippet**
```py
class SCart(BaseModel):
    customer_id: uuid.UUID
    cart_b64_hash: str
```

## Commit 14
**Message**: `feat(api): register api router and route modules`

```bash
git add backend/api/main.py backend/api/routes/__init__.py
git commit -m "feat(api): register api router and route modules"
```

**Snippet (`backend/api/main.py`)**
```py
api_router = APIRouter()
api_router.include_router(product.router, prefix="/product", tags=["product"])
api_router.include_router(cart.router, prefix="/cart", tags=["cart"])
```

## Commit 15
**Message**: `feat(api-product): implement list and detail endpoints`

```bash
git add backend/api/routes/product.py
git commit -m "feat(api-product): implement list and detail endpoints"
```

**Snippet**
```py
@router.get("/", response_model=list[SProduct])
async def get_products() -> list[SProduct]:
    return await ProductDAO.get_all()
```

## Commit 16
**Message**: `feat(api-cart): implement get and create cart endpoints`

```bash
git add backend/api/routes/cart.py
git commit -m "feat(api-cart): implement get and create cart endpoints"
```

**Snippet**
```py
@router.post("/")
async def add_cart(cart_data: SCart):
    cart_id = uuid.uuid4()
```

## Commit 17
**Message**: `feat(api-order): implement create and read order endpoints`

```bash
git add backend/api/routes/order.py
git commit -m "feat(api-order): implement create and read order endpoints"
```

**Snippet**
```py
for product in order_data.products:
    await OrdersListingDAO.add(order_id=order_id, product_id=product.product_id)
```

## Commit 18
**Message**: `feat(api-customer): implement customer registration endpoint`

```bash
git add backend/api/routes/customer.py
git commit -m "feat(api-customer): implement customer registration endpoint"
```

**Snippet**
```py
db_item = await CustomerDAO.get_one_or_none(customer_phone=customer_data.customer_phone)
if db_item:
    raise HTTPException(status_code=500, detail="User with this phone number already exists")
```

## Commit 19
**Message**: `feat(api-admin): add admin product and order management endpoints`

```bash
git add backend/api/routes/admin.py backend/api/schemas/admin.py
git commit -m "feat(api-admin): add admin product and order management endpoints"
```

**Snippet**
```py
@router.post("/product")
async def add_product(product_data: SAddProduct):
    product_id = uuid.uuid4()
```

## Commit 20
**Message**: `feat(app): bootstrap FastAPI entrypoint with cors and startup init`

```bash
git add backend/main.py
git commit -m "feat(app): bootstrap FastAPI entrypoint with cors and startup init"
```

**Snippet**
```py
app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000", "http://localhost:8888"])
app.include_router(api_router)
```

## Commit 21
**Message**: `feat(migration): add alembic config and initial migration`

```bash
git add backend/alembic.ini backend/alembic/env.py backend/alembic/script.py.mako backend/alembic/versions/d2db0ef204cb_initial_migration.py
git commit -m "feat(migration): add alembic config and initial migration"
```

**Snippet (`...initial_migration.py`)**
```py
op.create_table('customers', ...)
op.create_table('products', ...)
op.create_table('orders', ...)
```

## Commit 22
**Message**: `feat(frontend-init): scaffold svelte vite project`

```bash
git add frontend/package.json frontend/package-lock.json frontend/vite.config.js frontend/svelte.config.js frontend/jsconfig.json frontend/index.html frontend/public/vite.svg frontend/src/vite-env.d.ts
git commit -m "feat(frontend-init): scaffold svelte vite project"
```

**Snippet (`frontend/package.json`)**
```json
"scripts": {
  "dev": "vite",
  "build": "vite build"
}
```

## Commit 23
**Message**: `feat(frontend-core): add app entry and global styles`

```bash
git add frontend/src/main.js frontend/src/styles/main.scss
git commit -m "feat(frontend-core): add app entry and global styles"
```

**Snippet**
```js
import './styles/main.scss';
import App from './components/App/App.svelte';
```

## Commit 24
**Message**: `feat(frontend-layout): add container and app shell`

```bash
git add frontend/src/components/Container/Container.svelte frontend/src/components/Container/Container.scss frontend/src/components/App/App.svelte frontend/src/components/App/App.scss
git commit -m "feat(frontend-layout): add container and app shell"
```

**Snippet (`App.svelte`)**
```svelte
<Container><Header /></Container>
<Container><Menu /></Container>
<Container><PizzaCard /></Container>
```

## Commit 25
**Message**: `feat(frontend-header-menu): implement header navigation and cart state wiring`

```bash
git add frontend/src/components/Header/Header.svelte frontend/src/components/Header/Header.scss frontend/src/components/Menu/Menu.svelte frontend/src/components/Menu/Menu.scss frontend/src/components/Menu/types.ts frontend/src/store/pizza.store.ts
git commit -m "feat(frontend-header-menu): implement header navigation and cart state wiring"
```

**Snippet (`Menu.svelte`)**
```ts
const unsubscribe = pizzaStore.subscribe((currentStore) => {
  pizzaCart = currentStore;
});
```

## Commit 26
**Message**: `feat(frontend-catalog): add slider special catalog cart modal popup and data store`

```bash
git add frontend/src/components/Slider/Slider.svelte frontend/src/components/Slider/Slider.scss frontend/src/components/Slider/types.ts frontend/src/components/Special/Special.svelte frontend/src/components/Special/Special.scss frontend/src/components/PizzaCard/PizzaCard.svelte frontend/src/components/PizzaCard/PizzaCard.scss frontend/src/components/Cart/Cart.svelte frontend/src/components/Cart/Cart.scss frontend/src/components/Modal/Modal.svelte frontend/src/components/Modal/Modal.scss frontend/src/components/PopUp/PopUp.svelte frontend/src/components/PopUp/PopUp.scss frontend/src/store/data.store.ts frontend/Dockerfile frontend/nginx/default.conf

git commit -m "feat(frontend-catalog): add slider special catalog cart modal popup and data store"
```

**Snippet (`PizzaCard.svelte`)**
```ts
function addToCart(pizzaToAdd) {
  pizzaStore.update((currentPizzas) => {
    const updatedPizzas = currentPizzas.map((pizza) =>
      pizza.product_id === pizzaToAdd.product_id ? { ...pizza, count: pizza.count + 1 } : pizza
    );
    return updatedPizzas;
  });
}
```

**Snippet (`Cart.svelte`)**
```ts
$: sumOfCart = pizzaCart.reduce((total, pizza) => {
  return total + pizza.product_price * pizza.count;
}, 0);
```

---

## Как сделать frontend еще более атомарным (если препод смотрит строго)
Разбей `Commit 26` на 6 отдельных:
1. `feat(frontend-slider): add carousel component`
2. `feat(frontend-special): add special offers section`
3. `feat(frontend-catalog): add pizza grid and add-to-cart flow`
4. `feat(frontend-cart): add cart panel and item counters`
5. `feat(frontend-modal-popup): add order modal and popup notifications`
6. `chore(frontend): add data store and nginx/docker runtime config`

Это даст `31` коммит. Если надо ровно `20-30`, оставь как выше (`26`).

## Критично для "legit" вида
- Один коммит = одна идея.
- Не мешай backend+frontend в одном коммите (кроме финального интеграционного, как `26`).
- Не используй сообщения `update`, `fix`, `final` без контекста.
- После каждого 4-5 коммита делай `git log --oneline --graph -n 20` и проверяй читаемость истории.
