<script>
	import Container from '../Container/Container.svelte';
	import Header from '../Header/Header.svelte';
	import Menu from '../Menu/Menu.svelte';
</script>

<main>
	<Container>
		<Header />
	</Container>

	<Container>
		<Menu />
	</Container>
</main>

<style lang="scss">
	@import 'App.scss';
</style>
