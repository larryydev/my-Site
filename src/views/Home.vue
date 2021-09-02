<template>

  <div class="Home container">
    <img src="@/assets/homepageart.png" title="Things I care about">
    <h1>Hi, I am Larry Yu.</h1>
    <div id="about">      
      <p> I am a college student with a penchant for exploring technologies, and have multiple different interests. </p>
      <p> As you can see from the art above, I am passionate in quantum computing, automation, robotics, system thinking, and sustainbility. </p>
      <p> Feel free to reach out to me in any form of contact. </p>
    </div>
  </div>

</template>


<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
    
  }
}
</script>


<style scoped>


img {
  width: 45vw;
  padding-bottom: 50px;
}

#about {
  font-size: 22px;
  margin: 60px 25% 100px 33%;
  text-align: left;
}


</style>
