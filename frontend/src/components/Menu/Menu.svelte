<script lang="ts">
	import Cart from '../Cart/Cart.svelte';
	import { pizzaStore } from '../../store/pizza.store';
	import type { IPizzaCart } from './types';
	import { onDestroy } from 'svelte';

	let isOpenCart = false;
	let pizzaCart: IPizzaCart[];

	const unsubscribe = pizzaStore.subscribe((currentStore) => {
		pizzaCart = currentStore;
	});

	function toggle() {
		isOpenCart = !isOpenCart;
	}

	function deleteItem(pizzaId: CustomEvent) {
		pizzaCart = pizzaCart.filter((pizza) => pizza.id !== pizzaId.detail);
	}

	function increaseCount(pizzaId: CustomEvent) {
		pizzaCart = pizzaCart.map((pizza) => {
			if (pizza.id === pizzaId.detail) {
				return { ...pizza, count: pizza.count + 1 };
			}
			return pizza;
		});
	}

	function decreaseCount(pizzaId: CustomEvent) {
		pizzaCart = pizzaCart.map((pizza) => {
			if (pizza.id === pizzaId.detail && pizza.count > 1) {
				return { ...pizza, count: pizza.count - 1 };
			}
			return pizza;
		});
	}

	$: onDestroy(unsubscribe);
</script>

<nav>
	<ul>
		<li>
			<a href="#">Пицца</a>
		</li>
		<li>
			<a href="#">Паста</a>
		</li>
		<li>
			<a href="#">Супы</a>
		</li>
		<li>
			<a href="#">Салаты</a>
		</li>
		<li>
			<a href="#">Напитки</a>
		</li>
		<li>
			<a href="#">Десерты</a>
		</li>
		<li>
			<a href="#">Бакалея</a>
		</li>
		<li>
			<a href="#">Акции</a>
		</li>
		<li>
			<a href="#">Комбо</a>
		</li>
		<li>
			<a href="#">Контакты</a>
		</li>
	</ul>

	<button on:click={toggle}>Корзина <span>{pizzaCart.length}</span></button>

	{#if isOpenCart}
		<Cart
			{pizzaCart}
			on:deleteItem={deleteItem}
			on:increaseCount={increaseCount}
			on:decreaseCount={decreaseCount}
		/>
	{/if}
</nav>

<style lang="scss">
	@import 'Menu.scss';
</style>
