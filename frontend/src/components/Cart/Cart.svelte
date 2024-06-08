<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { fade, slide } from 'svelte/transition';
	import type { IPizzaCart } from '../Menu/types';

	export let pizzaCart: IPizzaCart[] = [];
	const dispatch = createEventDispatcher();

	$: sumOfCart = pizzaCart.reduce((total, pizza) => {
		return total + pizza.price * pizza.count;
	}, 0);

	function deletePizzaFromCart(pizzaId: string) {
		dispatch('deleteItem', pizzaId);
	}

	function increaseCount(pizzaId: string) {
		dispatch('increaseCount', pizzaId);
	}

	function decreaseCount(pizzaId: string) {
		dispatch('decreaseCount', pizzaId);
	}
</script>

<div class="cart" transition:fade={{ duration: 300 }}>
	{#each pizzaCart as pizza}
		<div class="cart__item" transition:slide>
			<div class="cart__img">
				<img src={pizza.img} alt={pizza.title} />
			</div>
			<div class="cart__info">
				<h3>{pizza.title}</h3>
				<div class="cart__count">
					<button on:click={() => decreaseCount(pizza.id)}>-</button>
					<span>{pizza.count}</span>
					<button on:click={() => increaseCount(pizza.id)}>+</button>
				</div>
			</div>
			<div class="cart__total">
				<button on:click={() => deletePizzaFromCart(pizza.id)}>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
						<circle cx="12" cy="12" r="10" stroke-width="1.5" />
						<path
							d="M14.5 9.50002L9.5 14.5M9.49998 9.5L14.5 14.5"
							stroke-width="1.5"
							stroke-linecap="round"
						/>
					</svg>
				</button>
				<span>{pizza.price * pizza.count} ₽</span>
			</div>
		</div>
	{/each}

	<div class="cart__sum">
		<h3>Сумма заказа</h3>
		<div>{sumOfCart} ₽</div>
	</div>

	{#if sumOfCart > 0}
		<div class="cart__buy">
			<button>Оформить заказ</button>
		</div>
	{/if}
</div>

<style lang="scss">
	@import 'Cart.scss';
</style>
