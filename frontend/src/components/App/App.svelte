<script>
	import Container from '../Container/Container.svelte';
	import Header from '../Header/Header.svelte';
	import Menu from '../Menu/Menu.svelte';
	import Special from '../Special/Special.svelte';
	import Slider from '../Slider/Slider.svelte';
	import PizzaCard from '../PizzaCard/PizzaCard.svelte';
</script>

<main>
	<Container>
		<Header />
	</Container>

	<Container>
		<Menu />
	</Container>

	<Container>
		<Slider />
	</Container>

	<Container>
		<Special />
	</Container>

	<Container>
		<PizzaCard />
	</Container>
</main>

<style lang="scss">
	@import 'App.scss';
</style>
