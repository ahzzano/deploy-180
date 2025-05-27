<script lang="ts">
    import ModelResults from "../components/ModelResults.svelte";
    const { data } = $props();
</script>

<div class="hero">
    <div class="hero-content text-center">
        <div class="max-w-md">
            <h1 class="text-5xl font-bold">Banana Leaf Disease Classifier</h1>
            <p class="mt-2">Predicting the health of a Banana Leaf with AI</p>
            <button class="btn btn-primary">Get Started</button>
        </div>
    </div>
</div>

<div class="card bg-base-200 shadow-sm rounded-box">
    <div class="card-body">
        <span class="card-title">About</span>
        <p>
            Here is our final project for the course of CS 180 for A.Y.
            2024-2025
        </p>
    </div>
</div>

<div class="card bg-base-200 shadow-sm">
    <div class="card-body rounded-box">
        <span class="card-title">Models</span>
        <p>Here are the models showcased in our presentation</p>
        <div class="join join-vertical">
            <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
            <ModelResults
                title={"VGG19 + kNN"}
                route={"vgg19knn"}
                prediction={data.predictions.vgg19knn}
            />
            <ModelResults
                title={"Warmup + Cosine"}
                route={"cosine"}
                prediction={data.predictions.cosine}
            />
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
