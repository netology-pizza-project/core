import { readable } from 'svelte/store';

export const pizzasData = readable([
	{
		id: '1',
		img: 'src/assets/pizza/margarita.webp',
		title: 'Пицца "Маргарита"',
		price: 900,
		description:
			'Классическая и простая, с свежими томатами, сыром моцарелла, базиликом и оливковым маслом extra-virgin.',
		count: 1
	},
	{
		id: '2',
		img: 'src/assets/pizza/pepperoni.webp',
		title: 'Пицца с Пепперони',
		price: 1000,
		description: 'Любимец многих, щедро уложенная ломтиками пепперони и смесью сыров моцарелла и чеддер.',
		count: 1
	},
	{
		id: '3',
		img: 'src/assets/pizza/BBQ.webp',
		title: 'Пицца с Курицей BBQ',
		price: 700,
		description: 'Копченый соус BBQ, гриль-курица, красный лук и кинза, покрытые сыром моцарелла.',
		count: 1
	},
	{
		id: '4',
		img: 'src/assets/pizza/hawaiian.webp',
		title: 'Гавайская Пицца',
		price: 850,
		description:
			'Домашняя паста феттуччине, сливочный соус, креветки, трюфельное масло, черный перец, пармезан.350 г',
		count: 1
	},
	{
		id: '5',
		img: 'src/assets/pizza/vegetable.webp',
		title: 'Овощная Пицца',
		price: 750,
		description: 'Сад из сезонных овощей включая болгарский перец, лук, грибы и оливки, с фетой и сыром моцарелла.',
		count: 1
	},
	{
		id: '6',
		img: 'src/assets/pizza/buffalo.webp',
		title: 'Пицца с Курицей Баффало',
		price: 400,
		description: 'Острая соус Баффало, курица, сельдерей и крошки голубого сыра, с вихрем соуса ранч.',
		count: 1
	},
	{
		id: '7',
		img: 'src/assets/pizza/meat.webp',
		title: 'Пицца для Любителей Мяса',
		price: 1500,
		description: 'Наполненная пепперони, колбаской, ветчиной, беконом и говядиной, покрытая сыром моцарелла.',
		count: 1
	}
]);
