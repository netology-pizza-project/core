# Дерево задач и Git-истории (для защиты проекта)

## Цель
Собрать понятную историю разработки из текущего состояния проекта без мусорных коммитов вида `update ...`, `final` и смешения дневников с кодом.

## Правило "легитимно"
- Не придумывать функциональность, которой нет в коде.
- Делить существующий код на логичные инженерные задачи.
- Каждый коммит должен менять ограниченный набор файлов и объясняться одной фразой.

## Task Tree (25 задач)

### Sprint 0: Bootstrap и инфраструктура
1. `PIZ-01 repo-structure`: базовая структура репозитория и служебные каталоги.
2. `PIZ-02 dev-docs`: начальные документы в `_docs` и `README.md`.
3. `PIZ-03 docker-local`: локальная оркестрация в `infra/compose-local.yml`.
4. `PIZ-04 backend-docker`: контейнеризация backend (`backend/Dockerfile`, `backend/requirements.txt`).
5. `PIZ-05 frontend-docker-nginx`: контейнеризация frontend и nginx (`frontend/Dockerfile`, `frontend/nginx/default.conf`).

### Sprint 1: Backend foundation
6. `PIZ-06 app-init`: старт FastAPI приложения, CORS, подключение роутера (`backend/main.py`, `backend/api/main.py`).
7. `PIZ-07 db-core`: SQLAlchemy base/engine/session (`backend/db/base.py`, `backend/db/__init__.py`).
8. `PIZ-08 db-models-product-order`: модели `Product`, `Order`, `OrdersListing` (`backend/db/models.py`).
9. `PIZ-09 db-models-cart-customer`: модели `Cart`, `Customer` (`backend/db/models.py`).
10. `PIZ-10 alembic-init`: подключение Alembic (`backend/alembic.ini`, `backend/alembic/*`, `backend/alembic/versions/*`).
11. `PIZ-11 dao-base`: базовый DAO слой (`backend/dao/base.py`).
12. `PIZ-12 dao-entities`: DAO для product/cart/order/customer (`backend/dao/*.py`).

### Sprint 2: API и бизнес-операции
13. `PIZ-13 schema-product`: Pydantic-схемы продукта (`backend/api/schemas/product.py`).
14. `PIZ-14 schema-order`: Pydantic-схемы заказа (`backend/api/schemas/order.py`).
15. `PIZ-15 schema-cart-customer`: схемы корзины и клиента (`backend/api/schemas/cart.py`, `backend/api/schemas/customer.py`).
16. `PIZ-16 route-product`: endpoint чтения продуктов (`backend/api/routes/product.py`).
17. `PIZ-17 route-cart`: endpoint корзины (`backend/api/routes/cart.py`).
18. `PIZ-18 route-order`: создание/чтение заказа (`backend/api/routes/order.py`).
19. `PIZ-19 route-customer`: регистрация клиента (`backend/api/routes/customer.py`).
20. `PIZ-20 route-admin`: админ-операции product/order (`backend/api/routes/admin.py`).

### Sprint 3: Frontend
21. `PIZ-21 frontend-bootstrap`: Vite/Svelte конфигурация (`frontend/package.json`, `frontend/vite.config.js`, `frontend/svelte.config.js`).
22. `PIZ-22 app-layout`: базовый layout и контейнеры (`frontend/src/components/App/*`, `Container/*`, `Header/*`).
23. `PIZ-23 catalog-ui`: меню/слайдер/спецблоки/карточки (`Menu/*`, `Slider/*`, `Special/*`, `PizzaCard/*`).
24. `PIZ-24 cart-modal-popup`: корзина, модалка, popup (`Cart/*`, `Modal/*`, `PopUp/*`).
25. `PIZ-25 stores-assets-style`: stores, global styles, статические ассеты (`frontend/src/store/*`, `frontend/src/styles/main.scss`, `frontend/public/assets/*`).

## Git Tree (как оформить)

### Ветки
- `main`: оставить как есть (исторический шум не трогать).
- `codex/clean-history-for-teacher`: новая ветка только для демонстрации структуры задач.

### Безопасная подготовка
1. Зафиксируй текущие незакоммиченные изменения отдельным коммитом или `git stash`.
2. Создай новую ветку от текущего `main`.
3. Пересобери историю в 25 атомарных коммитов.

### Рекомендуемый сценарий команд
```bash
# 0) сохранить текущее состояние
git stash push -u -m "wip-before-clean-history"

# 1) новая ветка для преподавателя
git checkout -b codex/clean-history-for-teacher

# 2) превратить текущий снапшот в набор задач
# переносим HEAD к самому первому коммиту, но оставляем все изменения в рабочем дереве
ROOT=$(git rev-list --max-parents=0 HEAD | tail -n 1)
git reset --mixed "$ROOT"

# 3) далее повторить 25 раз:
#   - выбрать файлы одной задачи
#   - git add <файлы>
#   - git commit -m "PIZ-XX: <короткое действие>"

# 4) вернуть рабочие изменения (если были)
git stash pop
```

## Набор коммит-месседжей (готовый шаблон)

```text
PIZ-01: initialize repository layout and project folders
PIZ-02: add base docs and repository guide
PIZ-03: add local docker-compose orchestration
PIZ-04: containerize backend service
PIZ-05: containerize frontend and nginx gateway
PIZ-06: bootstrap FastAPI app and router wiring
PIZ-07: configure SQLAlchemy base and async engine
PIZ-08: add product and order domain models
PIZ-09: add cart and customer domain models
PIZ-10: initialize alembic migration setup
PIZ-11: add generic DAO base operations
PIZ-12: add entity DAOs for product/cart/order/customer
PIZ-13: add product API schemas
PIZ-14: add order API schemas
PIZ-15: add cart and customer API schemas
PIZ-16: implement product read endpoints
PIZ-17: implement cart endpoints
PIZ-18: implement order create/read endpoints
PIZ-19: implement customer registration endpoint
PIZ-20: implement admin product/order endpoints
PIZ-21: setup Svelte + Vite frontend scaffold
PIZ-22: implement application layout and header
PIZ-23: implement catalog UI components
PIZ-24: implement cart, modal and popup flows
PIZ-25: add stores, global styles and static assets
```

## Что показать преподавателю
- Task tree из 25 задач (этот документ).
- `git log --oneline --decorate --graph -n 40` из ветки `codex/clean-history-for-teacher`.
- Соответствие: `1 задача = 1 осмысленный коммит`.
