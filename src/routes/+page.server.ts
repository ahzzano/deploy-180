import { fail, type Actions } from "@sveltejs/kit";
import * as tf from "@tensorflow/tfjs"
import type { PageServerLoad } from "./$types";

const predictions = {
    vgg19knn: null,
    squeezenet: null
}

export const load: PageServerLoad = async () => {
    console.log(predictions)
    return {
        predictions: predictions
    }
}

export const actions = {
    vgg19knn: async ({ request }) => {

        const formData = await request.formData()

        const response = await fetch("http://localhost:8000/vgg19knn", {
            method: "POST",
            body: formData
        })
        const results = await response.json()
        predictions.vgg19knn = results.prediction
        return { success: true }
    }
} satisfies Actions;