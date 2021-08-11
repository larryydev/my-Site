<template>

<div id="footer">

<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">


<footer class="text-center text-lg-start text-muted">

  <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">

    <div class="me-5 d-none d-lg-block">
      <span></span>
    </div>

    <div id="contact">
      <a href="https://twitter.com/LJhYu4" class="me-4 text-reset">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="mailto: larryyu0116@gmail.com?subject=Greeting From My Site" class="me-4 text-reset">
        <i class="fab fa-google"></i>
      </a>
      <a href="https://www.linkedin.com/in/larryjunhongyu/" class="me-4 text-reset">
        <i class="fab fa-linkedin"></i>
      </a>
      <a href="https://github.com/ly0708" class="me-4 text-reset">
        <i class="fab fa-github"></i>
      </a>
    </div>
  </section>
  
</footer>


</div>

</template>


<script>

export default {
    name: "footer",
}

</script>



<style scoped>

#footer {
  position: fixed;
  bottom: 0;
  width: 100%;
}

#contact a{
    font-size: 25px;
}


</style>
