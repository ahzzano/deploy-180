<script lang="ts">
    import { enhance } from "$app/forms";
    import { slide } from "svelte/transition";
    import type { PageProps } from "../routes/$types";

    let { title, route, prediction } = $props();
    let isPredicting = $state(false);
</script>

<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
<div
    class="collapse collapse-arrow border border-base-300 join-item"
    tabindex="0"
>
    <input type="radio" name="accordion" checked={false} />
    <span class="collapse-title font-semibold">{title}</span>
    <div class="collapse-content">
        <div class="mt-4 flex flex-col gap-8">
            <span>Try our Model</span>
            {#if !isPredicting && prediction != null}
                <div class="alert alert-info" transition:slide>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6 shrink-0 stroke-current"
                        fill="none"
                        viewBox="0 0 24 24"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                    </svg>
                    <span>
                        {title} Prediction:
                        <span class="font-bold">
                            {prediction}
                        </span>
                    </span>
                </div>
            {/if}
            <form
                method="POST"
                action="?/{route}"
                class="flex"
                enctype="multipart/form-data"
                use:enhance={() => {
                    isPredicting = true;
                    return async ({ update }) => {
                        isPredicting = false;
                        update();
                    };
                }}
            >
                <div class="flex-1">
                    <input class="file-input" type="file" name="file" />
                </div>
                <button class="btn btn-primary" type="submit">Upload</button>
            </form>
        </div>
    </div>
</div>
