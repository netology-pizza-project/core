<script lang="ts">
	import { onMount } from 'svelte';
	import { pizzasData } from '../../store/data.store';
	import { pizzaStore } from '../../store/pizza.store';
	import PopUp from '../PopUp/PopUp.svelte';
	import type { IPizzaCart } from '../Menu/types';

	// TODO: удалить когда будет реализовано получение через API
	let pizzaDataList: IPizzaCart[] = [];

	let isShowPopUp = false;
	let timer: ReturnType<typeof setTimeout>;

	$: if (isShowPopUp) {
		timer = setTimeout(() => {
			isShowPopUp = !isShowPopUp;
		}, 1000);
	}

	let unsubscribe;

	async function getPizzaData() {
		try {
			const request = await fetch('http://localhost:8888/product', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					Accept: 'application/json'
				}
			});

			if (request.ok) {
				const pizzaList = await request.json();

				unsubscribe = pizzasData.subscribe(() => {
					pizzaDataList = pizzaList;
				});
			}
		} catch (e) {
			console.log(e);
		}
	}

	async function setPizzaData(productItem) {
		try {
			const request = await fetch('http://localhost:8888/admin/product', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					Accept: 'application/json'
				},
				body: JSON.stringify(productItem)
			});

			if (request.ok) {
				const response = await request.json();

				unsubscribe = pizzasData.subscribe(() => {
					pizzaDataList = response;
				});
			}
		} catch (e) {
			console.log(e);
		}
	}

	function addToCart(pizzaToAdd) {
		isShowPopUp = !isShowPopUp;

		pizzaStore.update((currentPizzas) => {
			console.log(pizzaToAdd);

			let pizzaFound = false;

			const updatedPizzas = currentPizzas.map((pizza) => {
				if (pizza.product_id === pizzaToAdd.product_id) {
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

	onMount(async () => {
		if (pizzaDataList.length === 0) {
			getPizzaData();
		} else {
			const products = [
				{
					product_image: './assets/pizza/margarita.webp',
					product_title: 'Пицца "Маргарита"',
					product_price: 900,
					product_description:
						'Классическая и простая, с свежими томатами, сыром моцарелла, базиликом и оливковым маслом extra-virgin.',
					product_is_new: true,
					product_is_available: true
				},
				{
					product_image: './assets/pizza/pepperoni.webp',
					product_title: 'Пицца с Пепперони',
					product_price: 1000,
					product_description:
						'Любимец многих, щедро уложенная ломтиками пепперони и смесью сыров моцарелла и чеддер.',
					product_is_new: true,
					product_is_available: true
				},
				{
					product_image: './assets/pizza/BBQ.webp',
					product_title: 'Пицца с Курицей BBQ',
					product_price: 700,
					product_description:
						'Копченый соус BBQ, гриль-курица, красный лук и кинза, покрытые сыром моцарелла.',
					product_is_new: true,
					product_is_available: true
				},
				{
					product_image: './assets/pizza/hawaiian.webp',
					product_title: 'Гавайская Пицца',
					product_price: 850,
					product_description:
						'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан. 350 г',
					product_is_new: true,
					product_is_available: true
				},
				{
					product_image: './assets/pizza/vegetable.webp',
					product_title: 'Овощная Пицца',
					product_price: 750,
					product_description:
						'Сад из сезонных овощей включая болгарский перец, лук, грибы и оливки, с фетой и сыром моцарелла.',
					product_is_new: true,
					product_is_available: true
				},
				{
					product_image: './assets/pizza/buffalo.webp',
					product_title: 'Пицца с Курицей Баффало',
					product_price: 400,
					product_description:
						'Острая соус Баффало, курица, сельдерей и крошки голубого сыра, с вихрем соуса ранч.',
					product_is_new: true,
					product_is_available: true
				},
				{
					product_image: './assets/pizza/meat.webp',
					product_title: 'Пицца для Любителей Мяса',
					product_price: 1500,
					product_description:
						'Наполненная пепперони, колбаской, ветчиной, беконом и говядиной, покрытая сыром моцарелла.',
					product_is_new: true,
					product_is_available: true
				}
			];

			for await (const pizza of products) {
				setPizzaData(pizza);
			}
		}
	});
</script>

<h2 class="Title_Main">Каталог</h2>

{#if isShowPopUp}
	<PopUp titlePopUp="Пицца добавлена в корзину" />
{/if}

<div class="grid-container">
	{#each pizzaDataList as pizza}
		<div class="content-container">
			<img src={pizza.product_image} alt={pizza.product_title} class="customImage" />
			<h3 class="imageTitle">{pizza.product_title}</h3>
			<p class="description">{pizza.product_description}</p>
			<div class="secondaryTitle_N_Button">
				<h2 class="secondaryTitle">{pizza.product_price} ₽</h2>
				<button class="customButton" on:click={() => addToCart(pizza)}>В корзину</button>
			</div>
		</div>
	{/each}
</div>

<style lang="scss">
	@import 'PizzaCard.scss';
</style>
