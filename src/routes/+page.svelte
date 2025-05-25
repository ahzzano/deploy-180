<script lang="ts">
    import { fade } from "svelte/transition";
</script>

<!-- <div class="card bg-base-200 shadow-sm rounded-box">
    <div class="card-body">
        <span class="card-title">Banana Leaf Classifier</span>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum, nulla
        est. Quam, distinctio corrupti sed saepe explicabo molestias totam minus
        alias hic eligendi modi provident atque reprehenderit, magni dolores pariatur!
    </div>
</div> -->
<div class="hero">
    <div class="hero-content text-center">
        <div class="max-w-md">
            <h1 class="text-5xl font-bold">Banana Leaf Classifier</h1>
            <p class="mt-2">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. In,
                dolor possimus quos maiores neque animi. Laudantium
                perspiciatis, unde provident enim modi, at nemo dolorum neque
                suscipit soluta ab quis molestias.
            </p>
            <button class="btn btn-primary">Get Started</button>
        </div>
    </div>
</div>

<div class="card bg-base-200 shadow-sm rounded-box">
    <div class="card-body">
        <span class="card-title">About</span>
        lorem ipsum dolor sit amet consectetur adipisicing elit. voluptatum, nulla
        est. quam, distinctio corrupti sed saepe explicabo molestias totam minus
        alias hic eligendi modi provident atque reprehenderit, magni dolores pariatur!
    </div>
</div>

<div class="card bg-base-200 shadow-sm">
    <div class="card-body rounded-box">
        <span class="card-title">Models</span>
        <p>Here are the models showcased in our presentation</p>
        <div class="join join-vertical">
            <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
            <div
                class="collapse collapse-arrow border border-base-300 join-item"
                tabindex="0"
            >
                <span class="collapse-title font-semibold">EfficientNet</span>
                <div class="collapse-content">Hello World!</div>
            </div>
            <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
            <div
                class="collapse collapse-arrow border border-base-300 join-item"
                tabindex="0"
            >
                <span class="collapse-title font-semibold">VGG19 + kNN</span>
                <div class="collapse-content">Bruh</div>
            </div>
            <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
            <div
                class="collapse collapse-arrow border border-base-300 join-item"
                tabindex="0"
            >
                <span class="collapse-title font-semibold">SqueezeNet</span>
                <div class="collapse-content">Bruh</div>
            </div>
        </div>
    </div>
</div>

<span class="text-2xl">Members</span>
<div class="grid grid-cols-3 gap-4">
    <div class="card bg-base-200">
        <div class="card-body">Hombres</div>
    </div>
    <div class="card bg-base-200">
        <div class="card-body">Volveran</div>
    </div>
    <div class="card bg-base-200">
        <div class="card-body">Hermanos</div>
    </div>
</div>
