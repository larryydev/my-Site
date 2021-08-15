<template>

<div id="navbar">

<header>

  <ul class="nav justify-content-end">

    <li class="nav-item">
      <router-link to="/" class="nav-link">/</router-link>
    </li>
    
    <li class="nav-item">
      <router-link to="/projects" class="nav-link">Projects</router-link>
    </li>
    <li class="nav-item">
      <router-link to="/work" class="nav-link">Work</router-link>
    </li>
    <li class="nav-item">
      <a href="https://larryyublog.deta.dev/" class="nav-link">Blog</a>
    </li>

  </ul>

</header>

</div>
</template>


<script>

export default {
    name: "navbar",
}

</script>



<style>

.nav {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  padding: 40px 50px 0 0;
}

.nav-link {
  color: #2c3e50;
}

.nav-link:hover {
  text-decoration: underline;
  background: #b4afaf;
}

</style>
