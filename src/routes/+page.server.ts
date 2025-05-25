import { fail, type Actions } from "@sveltejs/kit";
import * as tf from "@tensorflow/tfjs"

export const actions = {
    upload_input: async ({ request }) => {
        const formData = await request.formData()
        const targetModel = formData.get('model')
        let targetUrl = 'squeezenet'

        if (!targetModel) {
            return fail(400, { message: "no model found" })
        }

        if (targetModel == "cnnknn") {
            targetUrl = '/vgg19knn'
        }

        const response = await fetch(`http://localhost:8000/${targetUrl}`, {
            method: "POST",
            body: formData
        })
        console.log(await response.json())
        return { success: true, results: response.json() }
    }

} satisfies Actions;