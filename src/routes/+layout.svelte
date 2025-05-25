<script lang="ts">
	import "../app.css";

	let { children } = $props();
</script>

<!-- <div class="navbar bg-base-200 shadow-sm"></div> -->

<div
	class="mr-8 ml-8 md:mr-48 md:ml-48 xl:mr-96 xl:ml-96 mt-16 flex flex-col gap-8"
>
	{@render children()}
</div>
