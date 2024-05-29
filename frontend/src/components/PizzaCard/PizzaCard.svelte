<script lang="ts">
	import { onMount } from 'svelte';
	import { pizzasData } from '../../store/data.store';
	import { pizzaStore } from '../../store/pizza.store';
	import type { IPizzaCart } from '../Menu/types';

	// TODO: удалить когда будет реализовано получение через API
	let mockPizzaData: IPizzaCart[] = [];

	const unsubscribe = pizzasData.subscribe((currentStore) => {
		mockPizzaData = currentStore;
	});

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

	onMount(() => {
		return () => {
			unsubscribe();
		};
	});
</script>

<h2 class="Title_Main">Паста</h2>

<div class="grid-container">
	{#each mockPizzaData as pizza}
		<div class="content-container">
			<img src={pizza.img} alt={pizza.title} class="customImage" />
			<h3 class="imageTitle">{pizza.title}</h3>
			<p class="description">{pizza.description}</p>
			<div class="secondaryTitle_N_Button">
				<h2 class="secondaryTitle">{pizza.price} ₽</h2>
				<button class="customButton" on:click={() => addToCart(pizza)}>В корзину</button>
			</div>
		</div>
	{/each}
</div>

<style lang="scss">
	@import 'PizzaCard.scss';
</style>
