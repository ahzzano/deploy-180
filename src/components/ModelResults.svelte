<script lang="ts">
    import { enhance } from "$app/forms";

    let { modelName, title } = $props();
</script>

<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
<div
    class="collapse collapse-arrow border border-base-300 join-item"
    tabindex="0"
>
    <input type="radio" name="accordion" checked={false} />
    <span class="collapse-title font-semibold">{title}</span>
    <div class="collapse-content">
        <div class="mt-8">
            <span>Try our Model</span>
            <form
                method="POST"
                action="?/upload_input"
                class="flex"
                enctype="multipart/form-data"
                use:enhance={async () => {}}
            >
                <input name="model" value={modelName} hidden />
                <div class="flex-1">
                    <input class="file-input" type="file" name="file" />
                </div>
                <button class="btn btn-primary" type="submit">Upload</button>
            </form>
        </div>
    </div>
</div>
