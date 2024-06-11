<script lang="ts">
	import { flip } from 'svelte/animate';
	import { onMount, onDestroy } from 'svelte';
	import type { IImages } from './types';

	// TODO: делать запрос за картинками
	let images: IImages[] = [
		{ id: '0', path: './assets/slider/1.png' },
		{ id: '1', path: './assets/slider/2.png' },
		{ id: '2', path: './assets/slider/3.png' },
		{ id: '3', path: './assets/slider/4.png' }

		// { id: '0', path: 'src/assets/pizza/margarita.webp' },
		// { id: '1', path: 'src/assets/pizza/pepperoni.webp' },
		// { id: '2', path: 'src/assets/pizza/BBQ.webp' },
		// { id: '3', path: 'src/assets/pizza/hawaiian.webp' },
		// { id: '4', path: 'src/assets/pizza/vegetable.webp' },
		// { id: '5', path: 'src/assets/pizza/buffalo.webp' },
		// { id: '6', path: 'src/assets/pizza/meat.webp' },

	];
	const speed = 500;

	const autoplay = true;
	const autoplaySpeed = 2000;

	let interval: ReturnType<typeof setInterval>;

	function updateOpacity(id: string, opacity: string) {
		const imageElement = document.getElementById(String(id));

		if (imageElement) {
			imageElement.style.opacity = opacity;
		}
	}

	function rotateLeft() {
		const transitioningImage = images[images.length - 1];

		updateOpacity(transitioningImage.id, '0');
		images = [images[images.length - 1], ...images.slice(0, images.length - 1)];

		setTimeout(() => updateOpacity(transitioningImage.id, '1'), speed);
	}

	function rotateRight() {
		const transitioningImage = images[0];

		updateOpacity(transitioningImage.id, '0');
		images = [...images.slice(1, images.length), images[0]];

		setTimeout(() => updateOpacity(transitioningImage.id, '1'), speed);
	}

	function startAutoPlay() {
		if (autoplay) {
			interval = setInterval(rotateLeft, autoplaySpeed);
		}
	}

	function stopAutoPlay() {
		clearInterval(interval);
	}

	onMount(() => {
		if (autoplay) {
			startAutoPlay();
		}
	});

	onDestroy(stopAutoPlay);
</script>

<!-- svelte-ignore a11y-mouse-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="carousel" on:mouseover={stopAutoPlay} on:mouseout={startAutoPlay}>
	<div class="carousel__container">
		<div class="carousel__images">
			{#each images as image (image.id)}
				<!-- svelte-ignore a11y-mouse-events-have-key-events -->
				<img src={image.path} alt="item" id={image.id} animate:flip={{ duration: speed }} />
			{/each}
		</div>
		<!-- svelte-ignore a11y-mouse-events-have-key-events -->
		<button class="carousel__btn" id="left" on:click={rotateLeft}>
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
				<path
					d="M14.2893 5.70708C13.8988 5.31655 13.2657 5.31655 12.8751 5.70708L7.98768 10.5993C7.20729 11.3805 7.2076 12.6463 7.98837 13.427L12.8787 18.3174C13.2693 18.7079 13.9024 18.7079 14.293 18.3174C14.6835 17.9269 14.6835 17.2937 14.293 16.9032L10.1073 12.7175C9.71678 12.327 9.71678 11.6939 10.1073 11.3033L14.2893 7.12129C14.6799 6.73077 14.6799 6.0976 14.2893 5.70708Z"
					fill="#0F0F0F"
				/>
			</svg>
		</button>
		<!-- svelte-ignore a11y-mouse-events-have-key-events -->
		<button class="carousel__btn" id="right" on:click={rotateRight}>
			<svg transform={'rotate(180)'} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
				<path
					d="M14.2893 5.70708C13.8988 5.31655 13.2657 5.31655 12.8751 5.70708L7.98768 10.5993C7.20729 11.3805 7.2076 12.6463 7.98837 13.427L12.8787 18.3174C13.2693 18.7079 13.9024 18.7079 14.293 18.3174C14.6835 17.9269 14.6835 17.2937 14.293 16.9032L10.1073 12.7175C9.71678 12.327 9.71678 11.6939 10.1073 11.3033L14.2893 7.12129C14.6799 6.73077 14.6799 6.0976 14.2893 5.70708Z"
					fill="#0F0F0F"
				/>
			</svg>
		</button>
	</div>
</div>

<style lang="scss">
	@import './Slider.scss';
</style>
