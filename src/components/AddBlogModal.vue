<template>

<div id="addblog">

<div class="modal" id="addblogModal" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="addblogModalLabel">Add Blog</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="mb-3">
                        <label for="key" class="form-label">API Key</label>
                        <input type="text" class="form-control" v-model="key">
                    </div>
                    <div class="mb-3">
                        <label for="title" class="form-label">Title</label>
                        <input type="text" class="form-control" v-model="title">
                    </div>

                    <div class="mb-3">
                        <label for="content" class="form-label">Content</label>
                        <textarea class="form-control" rows="5" v-model="content"></textarea>
                    </div>
                    <button type="submit" class="btn btn-secondary btn-sm" style="float: right;" @click="submit">Add</button>
                </form>
            </div>
        </div>
    </div>
</div>

    
</div>

</template>


<script>

import axios from "axios"

export default {
    name: "addblog",
    data() {
        return {
            title: "",
            content: "",
            key: ""
        };
    },
    methods: {

        sleep(milliseconds) {
            const date = Date.now();
            let currentDate = null;
            do {
                currentDate = Date.now();
            } while (currentDate - date < milliseconds);
        },

        submit() {
            var base_url = "https://38vaq8.deta.dev/"

            axios.put(base_url + "blog", {
                "title": this.title,
                "content": this.content
            }, {
                withCredentials: false,
                headers: {
                    "Content-Type": "application/json",
                    "X-API-Key": "h8mWXY88.bBEC8CWmjJmhnRmSdkMuZB-t4W48phcxu"
                }
            }).then(response => {
                console.log(response)
            });
            
            console.log("Submit")

            this.sleep(5000)
        },


    }
}
</script>


<style scoped>

.modal {
    top: 25px;
}




</style>