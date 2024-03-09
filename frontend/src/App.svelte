<script>
	import Container from './components/Container.svelte';
	import Header from './components/Header.svelte';
	import Menu from './components/Menu/Menu.svelte';
</script>

<main>
	<Container>
		<Header />
	</Container>

	<Container>
		<Menu />
	</Container>
</main>

<style>
	main {
		width: 100%;
		height: 100vh;
	}
</style>
