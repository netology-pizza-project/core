<script lang="ts">
	import { createEventDispatcher } from 'svelte';
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

<div class="cart">
	{#each pizzaCart as pizza}
		<div class="cart__item">
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
				<button on:click={() => deletePizzaFromCart(pizza.id)}>x</button>
				<span>{pizza.price * pizza.count}</span>
			</div>
		</div>
	{/each}

	<div class="cart__sum">{sumOfCart}</div>
</div>

<style lang="scss">
	@import 'Cart.scss';
</style>
