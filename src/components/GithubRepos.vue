<template>

    <div id="github">
                <div class="container">
            <h4 style="text-align: left;">Open Source</h4>
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                    <tr>
                    <th>Name</th>
                    <th>Language</th>
                    <th style="width: 50%">Description</th>
                </tr>
                </thead>
                <tbody>
                    <tr v-for="repo in repos" v-bind:key="repo.id">
                    <td v-if="repo.fork">{{ repo.name }}</td>
                    <td v-if="repo.fork">{{ repo.language }}</td>
                    <td v-if="repo.fork">{{ repo.description }}</td>
                </tr>
                </tbody>
            </table>
        </div>

        <div class="container">
            <h4 style="text-align: left;">Personal</h4>
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                    <tr>
                    <th>Name</th>
                    <th>Language</th>
                    <th style="width: 50%">Description</th>
                </tr>
                </thead>
                <tbody>
                    <tr v-for="repo in repos" v-bind:key="repo.id">
                    <td v-if="!repo.fork">{{ repo.name }}</td>
                    <td v-if="!repo.fork">{{ repo.language }}</td>
                    <td v-if="!repo.fork">{{ repo.description }}</td>
                </tr>
                </tbody>
            </table>
        </div>


        <button class="btn btn-primary" 
                data-bs-target="#collapseTarget" 
                data-bs-toggle="collapse" >
        Go to my Github Page
        </button>
        <div class="collapse py-2" id="collapseTarget">
            <p>For your security. Never trust a link.<br>
                !!! ALWAYS copy and paste the url yourself !!! <br>
                <u>{{url}}</u>
            </p>
        </div>

    </div>

</template>


<script>
import axios from "axios";

export default {
    name: "githubrepos",
    data() {
        return {
            url: "https://github.com/ly0708",
            repos: null,
        };
    },
    created: function () {
        axios.get("https://api.github.com/users/ly0708/repos").then((response) => {
            this.repos = response.data;
        });
    },
}

</script>


<style scoped>

</style>