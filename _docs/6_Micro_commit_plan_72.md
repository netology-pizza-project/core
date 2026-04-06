# Micro-Commit Plan (72 Commits)

Цель: раздробить историю на мелкие, правдоподобные шаги (`72` коммита), чтобы дерево задач и git-история выглядели естественно.

Правило: это план коммитов. Полные тела файлов бери из [5_Full_commit_by_commit_manual.md](/Users/epmak/ws/ed/Python/core/_docs/5_Full_commit_by_commit_manual.md).

## Phase A — Repo and Infra (10)
1. `chore(repo): add root readme skeleton` — `README.md`
2. `chore(docs): add repository structure doc` — `_docs/1_Описание структуры репозитория.md`
3. `chore(docs): add tooling setup doc` — `_docs/2_Настройка инструментов разработки.md`
4. `build(make): add compose wrapper commands` — `Makefile`
5. `chore(git): add gitignore rules` — `.gitignore`
6. `chore(docker): add dockerignore rules` — `.dockerignore`
7. `infra(compose): add postgres service` — `infra/compose-local.yml`
8. `infra(compose): add backend service wiring` — `infra/compose-local.yml`
9. `infra(compose): add frontend service wiring` — `infra/compose-local.yml`
10. `infra(compose): add networks and healthcheck` — `infra/compose-local.yml`

## Phase B — Backend Base (16)
11. `feat(backend): add python dependencies` — `backend/requirements.txt`
12. `feat(backend): add dockerfile base image and workdir` — `backend/Dockerfile`
13. `feat(backend): add prestart migration script` — `backend/utils/pre_start.sh`
14. `feat(config): add pydantic settings base` — `backend/core/config.py`
15. `feat(config): add postgres settings and db url property` — `backend/core/config.py`
16. `chore(core): init core package` — `backend/core/__init__.py`
17. `feat(db): initialize async engine` — `backend/db/base.py`
18. `feat(db): add async session maker` — `backend/db/base.py`
19. `feat(db): add declarative base` — `backend/db/base.py`
20. `chore(db): init db package` — `backend/db/__init__.py`
21. `feat(db): add uuid extension entity` — `backend/db/uuid.py`
22. `feat(model): add product model` — `backend/db/models.py`
23. `feat(model): add order model` — `backend/db/models.py`
24. `feat(model): add orders listing model` — `backend/db/models.py`
25. `feat(model): add cart model` — `backend/db/models.py`
26. `feat(model): add customer model` — `backend/db/models.py`

## Phase C — DAO Layer (10)
27. `feat(dao): add base DAO read methods` — `backend/dao/base.py`
28. `feat(dao): add base DAO write methods` — `backend/dao/base.py`
29. `chore(dao): init dao package` — `backend/dao/__init__.py`
30. `feat(dao-product): add product dao class` — `backend/dao/product.py`
31. `feat(dao-product): add product update method` — `backend/dao/product.py`
32. `feat(dao-cart): add cart dao class` — `backend/dao/cart.py`
33. `feat(dao-order): add order dao class` — `backend/dao/order.py`
34. `feat(dao-order): add order update method` — `backend/dao/order.py`
35. `feat(dao-order): add orders listing dao` — `backend/dao/order.py`
36. `feat(dao-customer): add customer dao class` — `backend/dao/customer.py`

## Phase D — Schemas and Routes (16)
37. `feat(schema-product): add read model` — `backend/api/schemas/product.py`
38. `feat(schema-product): add create model` — `backend/api/schemas/product.py`
39. `feat(schema-order): add order payload models` — `backend/api/schemas/order.py`
40. `feat(schema-order): add order read/update models` — `backend/api/schemas/order.py`
41. `feat(schema-cart): add cart models` — `backend/api/schemas/cart.py`
42. `feat(schema-customer): add customer model` — `backend/api/schemas/customer.py`
43. `feat(schema-admin): add admin schema placeholder` — `backend/api/schemas/admin.py`
44. `chore(schema): init schema package` — `backend/api/schemas/__init__.py`
45. `feat(route-product): add product list endpoint` — `backend/api/routes/product.py`
46. `feat(route-product): add product details endpoint` — `backend/api/routes/product.py`
47. `feat(route-cart): add get cart endpoint` — `backend/api/routes/cart.py`
48. `feat(route-cart): add create cart endpoint` — `backend/api/routes/cart.py`
49. `feat(route-order): add get order endpoint` — `backend/api/routes/order.py`
50. `feat(route-order): add create order and listing items` — `backend/api/routes/order.py`
51. `feat(route-customer): add customer registration endpoint` — `backend/api/routes/customer.py`
52. `feat(route-admin): add admin product/order endpoints` — `backend/api/routes/admin.py`

## Phase E — API/App Wiring and Migration (10)
53. `feat(api): create api router entry` — `backend/api/main.py`
54. `feat(api): register product and cart routers` — `backend/api/main.py`
55. `feat(api): register order admin customer routers` — `backend/api/main.py`
56. `chore(api): init api package and routes package` — `backend/api/__init__.py`, `backend/api/routes/__init__.py`
57. `feat(app): add FastAPI app factory basics` — `backend/main.py`
58. `feat(app): add cors middleware setup` — `backend/main.py`
59. `feat(app): add startup db init and include router` — `backend/main.py`
60. `feat(migration): add alembic ini and template` — `backend/alembic.ini`, `backend/alembic/script.py.mako`, `backend/alembic/README`
61. `feat(migration): add alembic env wiring` — `backend/alembic/env.py`
62. `feat(migration): add initial schema migration` — `backend/alembic/versions/d2db0ef204cb_initial_migration.py`

## Phase F — Frontend Core (10)
63. `feat(frontend): init package scripts and deps` — `frontend/package.json`, `frontend/package-lock.json`
64. `feat(frontend): add vite and svelte configs` — `frontend/vite.config.js`, `frontend/svelte.config.js`, `frontend/jsconfig.json`
65. `feat(frontend): add html entry and vite env types` — `frontend/index.html`, `frontend/src/vite-env.d.ts`, `frontend/public/vite.svg`
66. `feat(frontend): add app main entrypoint` — `frontend/src/main.js`
67. `feat(frontend): add global styles and font imports` — `frontend/src/styles/main.scss`
68. `feat(store): add cart store` — `frontend/src/store/pizza.store.ts`
69. `feat(store): add product data store` — `frontend/src/store/data.store.ts`
70. `feat(frontend-layout): add app/container shell` — `frontend/src/components/App/App.svelte`, `frontend/src/components/App/App.scss`, `frontend/src/components/Container/Container.svelte`, `frontend/src/components/Container/Container.scss`
71. `feat(frontend-header): add header component and styles` — `frontend/src/components/Header/Header.svelte`, `frontend/src/components/Header/Header.scss`
72. `feat(frontend-runtime): add nginx config and frontend docker image` — `frontend/nginx/default.conf`, `frontend/Dockerfile`

## Optional Extension to 90+ commits
Если преподаватель просит еще глубже, расширяй за счет UI-компонентов (каждый в 2 коммита: markup + style):
- `Menu`, `Slider`, `Special`, `PizzaCard`, `Cart`, `Modal`, `PopUp`.
- Отдельно: `types.ts` рядом с компонентами.
- Отдельно: статические ассеты (`frontend/public/assets/**`) и SQL seeds (`backend/db/seed/*.sql`).

Это легко доводит историю до `90–100` коммитов без фальшивых сообщений типа `update/final`.
