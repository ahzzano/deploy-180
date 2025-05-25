<script lang="ts">
	import "../app.css";

	let { children } = $props();
</script>

<div class="navbar bg-base-200 shadow-sm"></div>

<div class="pr-96 pl-96 mt-16 flex flex-col gap-8">
	{@render children()}
</div>
