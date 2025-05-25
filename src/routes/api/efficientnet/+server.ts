import { json } from "@sveltejs/kit";

export async function POST() {

    console.log("%sveltekit.assets%/squeezenet.weights.h5")
    return json(100)
}