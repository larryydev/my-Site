<template>

  <div id="main">

    <Navbar />

    <router-view />

    <Footer />

  </div>

</template>


<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'


export default {
    name: "app",
    components: {
      Navbar,
      Footer
    }
}

</script>



<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia, serif;
  text-align: center;
  color: #2c3e50;
}

img {
  width: 50vw;
}

</style>
