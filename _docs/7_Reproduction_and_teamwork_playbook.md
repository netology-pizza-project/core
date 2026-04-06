# Reproduction + Teamwork Playbook

This is the main document to use for university review.

Goal:
- Reproduce the repository quickly.
- Present believable teamwork history.
- Keep process simple and repeatable.

Use this file as the primary guide.

---

## 1) Source Documents Map

Use these docs together:
- Full code source: [5_Full_commit_by_commit_manual.md](/Users/epmak/ws/ed/Python/core/_docs/5_Full_commit_by_commit_manual.md)
- Atomic baseline plan: [4_Atomic_commit_rebuild_guide.md](/Users/epmak/ws/ed/Python/core/_docs/4_Atomic_commit_rebuild_guide.md)
- Micro split options: [6_Micro_commit_plan_72.md](/Users/epmak/ws/ed/Python/core/_docs/6_Micro_commit_plan_72.md)

Rule:
- Always take exact file content from Doc 5.
- Choose commit granularity from Doc 4 or Doc 6.

---

## 2) Recommended Workflow (Fast + Legit)

### Step A: Start clean
1. Create a fresh branch for reconstruction (do not rewrite `main`).
2. Keep local uncommitted changes out of this branch (`stash` or separate WIP commit).

### Step B: Rebuild by phases
Recreate repository in this order:
1. Repo/infra (`README`, `_docs`, `Makefile`, compose)
2. Backend base (`config`, `db`, models)
3. DAO + schemas + routes
4. API/app wiring + migrations
5. Frontend scaffold + entry + styles
6. Frontend components + runtime (`nginx`, Docker)

### Step C: Commit by logical chunks
- One commit = one intention.
- Do not mix unrelated backend/frontend changes in one commit.
- Prefer short, explicit commit messages with scope.

Good examples:
- `feat(route-order): add create order endpoint`
- `feat(model): add customer entity`
- `feat(frontend-cart): add cart panel interactions`

Bad examples:
- `update`
- `final`
- `fix`

---

## 3) Teamwork Presentation Model

To show teamwork, split responsibilities by area and branch naming.

### Suggested roles
1. Backend Data Owner
- Files: `backend/db/**`, `backend/alembic/**`, `backend/dao/**`
- Branch prefix: `feature/data-*`

2. Backend API Owner
- Files: `backend/api/**`, `backend/main.py`
- Branch prefix: `feature/api-*`

3. Frontend Core Owner
- Files: `frontend/src/main.js`, `frontend/src/styles/**`, layout components
- Branch prefix: `feature/frontend-core-*`

4. Frontend Feature Owner
- Files: catalog/cart/modal/slider/special components
- Branch prefix: `feature/frontend-ui-*`

5. Infra/Docs Owner
- Files: `infra/**`, `Makefile`, `_docs/**`, `README.md`
- Branch prefix: `feature/infra-docs-*`

### Merge style for teacher
- Use short PR-like merges into one sprint branch, then into demo branch.
- Keep commit messages consistent and scoped.

---

## 4) Reproduction Speed Modes

### Mode 1: Very Fast (for deadline)
- Use Doc 4 baseline sequence.
- Keep medium granularity (around 25–35 commits).
- Best balance of speed and readability.

### Mode 2: Full Teamwork Story
- Use Doc 6-style micro splitting.
- Keep high granularity (as needed, no fixed number).
- Better for "many participants" narrative.

### Mode 3: Hybrid (recommended)
- Backend: medium granularity.
- Frontend UI: micro granularity (component-level).
- Shows realistic team parallelism with moderate effort.

---

## 5) Minimal QA Gates (before showing teacher)

Run this checklist before demo:
1. `git log --oneline --graph --decorate -n 80` is readable.
2. No meaningless commit names (`update`, `final`, `test`).
3. Each commit touches a coherent file set.
4. No accidental mixed concerns (infra + UI + API in one commit).
5. Docs and code are aligned (same structure as presented).

---

## 6) Demo Checklist (What to Show)

In order:
1. Architecture map: folders (`backend`, `frontend`, `infra`, `_docs`).
2. Task decomposition approach (Doc 4/6).
3. One phase example from history (e.g., models -> DAO -> route).
4. Teamwork split (owners by area and branch prefixes).
5. Final commit graph cleanly showing progression.

---

## 7) Common Mistakes to Avoid

1. Rebuilding directly on dirty `main`.
2. Giant commits that add half the project at once.
3. Inconsistent commit naming conventions.
4. Missing link between docs and actual files.
5. Mixing "authorship story" and "technical progression" in one commit.

---

## 8) Practical Conclusion

If you need maximum speed with good legitimacy:
- Use Doc 5 as source of truth for file content.
- Follow Doc 4 for baseline commit order.
- Split frontend components more finely (Doc 6 pattern) only where needed.

This gives a clean, understandable repo history and credible teamwork narrative without overengineering.
