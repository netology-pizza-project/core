<script>
	import Container from '../Container/Container.svelte';
	import Header from '../Header/Header.svelte';
	import Menu from '../Menu/Menu.svelte';
	import Slider from '../Slider/Slider.svelte';

	let images = [
		{ id: 0, path: 'src/assets/slider/1.png' },
		{ id: 1, path: 'src/assets/slider/2.png' },
		{ id: 2, path: 'src/assets/slider/3.png' },
		{ id: 3, path: 'src/assets/slider/4.png' }
	];
</script>

<main>
	<Container>
		<Header />
	</Container>

	<Container>
		<Menu />
	</Container>

	<Container>
		<Slider
			{images}
			imageWidth={250}
			imageSpacing={15}
			controlColor={'white'}
			controlScale={0.8}
			displayControls={true}
			autoplay={true}
			autoplaySpeed={3000}
		/>
	</Container>
</main>

<style lang="scss">
	@import 'App.scss';
</style>
