<script lang="ts">
	import { fade, fly } from 'svelte/transition';

	export let titlePopUp = '';
</script>

<!-- svelte-ignore missing-declaration -->
<div class="pop-up" in:fly={{ y: 300, duration: 500 }} out:fade>
	<div class="pop-up__title">
		<h3>{titlePopUp}</h3>
		<span>
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20">
				<path fill="none" d="M0 0h24v24H0z" />
				<path fill="green" d="M9 16.172l-3.536-3.536-1.414 1.414L9 19 19.95 8.05l-1.414-1.414z" />
			</svg>
		</span>
	</div>

	<!-- <a href="#top">Перейти в корзину</a> -->
</div>

<style lang="scss">
	@import './PopUp.scss';
</style>
