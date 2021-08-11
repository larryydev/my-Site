<template>

  <div id="projects">
    <h2>Projects</h2>
    <GithubRepos />
  </div>
  
</template>

<script>
import GithubRepos from '../components/GithubRepos.vue'

export default {
  name: 'projects',
  components: {
    GithubRepos,
  }
}
</script>

<style scoped>
h3 {
  padding-bottom: 15px;
}

</style>