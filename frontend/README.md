# Документация для запуска frontend части проекта

## Рекомендуемая ide для разработки и её расширения

[VS Code](https://code.visualstudio.com/) + [Svelte](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

## Необходимое инструменты

[Node.js](https://nodejs.org/en) (выбираем LTS версию и скачиваем её)

[Git](https://git-scm.com/) (если у кого-то до сих пор нет)

## Начальная инициализация

<u><b>Переходим в папку frontend</b></u> и запускаем следующие команды в терминале

```sh
npm i
npm run dev
```

npm i - устанавливает все зависимости из файла package.json (только после клонирования репозитория, больше запускать её не нужно)

npm run dev - запускает проект для разработки (вводим каждый раз когда будете писать код)

## Ссылки на ресурсы проекта:
- [Макет](https://pixso.net/app/editor/7T6KyAj3UPnzfrIGdgcWbw?icon_type=1&page-id=0%3A1) (страница Homepage)

- [Jira](https://pipizza.atlassian.net/jira/software/projects/PIZ/boards/1)

- [GitHub](https://github.com/netology-pizza-project/core)

## Конечная сборка проекта

<u><b>Переходим в папку frontend</b></u> и запускаем следующую команду в терминале

```sh
npm run build
```
После выполнения команды, появиться папка __dist__. В ней содержится весь фронтенд проекта
