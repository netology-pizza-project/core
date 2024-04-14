<script lang="ts">
	import { pizzaStore } from '../../store/pizza.store';
	import type { IPizzaCart } from '../Menu/types';

	// TODO: удалить когда будет реализовано получение через API
	const mockPizzaData: IPizzaCart[] = [
		{
			id: '1',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 1',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '2',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 2',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '3',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 3',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '4',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 4',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '5',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 5',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '6',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 6',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '7',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 7',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		},
		{
			id: '8',
			img: 'src/assets/special/spec_piz_1.png',
			title: 'с креветками и трюфелями 8',
			price: 600,
			description:
				'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
			count: 1
		}
	];

	function addToCart(pizzaToAdd) {
		pizzaStore.update((currentPizzas) => {
			let pizzaFound = false;

			const updatedPizzas = currentPizzas.map((pizza) => {
				if (pizza.id === pizzaToAdd.id) {
					pizzaFound = true;

					return { ...pizza, count: pizza.count + 1 };
				}

				return pizza;
			});

			if (!pizzaFound) {
				updatedPizzas.push({ ...pizzaToAdd, count: 1 });
			}

			return updatedPizzas;
		});
	}
</script>

<h2 class="Title_Main">Паста</h2>

<div class="grid-container">
	{#each mockPizzaData as pizza}
		<div class="content-container">
			<img src={pizza.img} alt={pizza.title} class="customImage" />
			<h3 class="imageTitle">{pizza.title}</h3>
			<p class="description">{pizza.description}</p>
			<div class="secondaryTitle_N_Button">
				<h2 class="secondaryTitle">От {pizza.price} ₽</h2>
				<button class="customButton" on:click={() => addToCart(pizza)}>В корзину</button>
			</div>
		</div>
	{/each}
</div>

<style lang="scss">
	@import 'PizzaCard.scss';
</style>
