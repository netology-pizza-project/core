<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let canClose = true;
	export let className = '';
	export let dialog = null;
	export let icon = undefined;
	export let title = '';

	$: classNames = 'dialog' + (className ? ' ' + dialog : '');

	function close() {
		dispatch('close');
		dialog.close();
	}
</script>

<dialog bind:this={dialog} class={classNames}>
	<header>
		{#if icon}
			{icon}
		{/if}
		<div class="title">{title}</div>
		{#if canClose}
			<button class="close-btn" on:click={close}> &#x2716; </button>
		{/if}
	</header>

	<main>
		<slot />
	</main>
</dialog>

<style>
	.body {
		padding: 10px;
	}

	.close-btn {
		background-color: transparent;
		border: none;
		color: rgb(247, 210, 45);
		font-size: 24px;
		outline: none;
		margin: 0;
		padding: 0;
		cursor: pointer;
	}

	dialog {
		/* These properties center the dialog in the browser window. */
		position: fixed;

		border-radius: 12px;
		padding: 0;
		border: none;

		box-shadow:
			0px 4px 28px 0px rgba(0, 0, 0, 0.08),
			0px 4px 28px 0px rgba(0, 0, 0, 0.08);
		background: rgb(255, 255, 255);
	}

	header {
		display: flex;
		justify-content: space-between;
		align-items: center;

		box-sizing: border-box;
		color: white;
		font-weight: bold;
		padding: 10px;
		width: 100%;
	}

	main {
		padding: 10px;
	}

	.title {
		color: rgb(247, 210, 45);
		font-family: Montserrat;
		font-size: 32px;
		font-weight: 800;
		line-height: 17px;
		letter-spacing: 0%;
		text-align: left;
	}

	dialog::backdrop,
	:global(dialog + .backdrop) {
		/* This is a transparent shade of gray. */
		/* Why is this ignored in Safari? */
		background: rgba(247, 210, 45, 0.4);
	}
</style>
