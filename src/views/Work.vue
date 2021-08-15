<template>

  <div id="workhistory" class="container">

    <h2>Work history</h2>
    <h5 style="padding: 45px 0 45px 0;">List of places that I’ve worked.</h5>

    

    <WorkTemplate companyname="Tyler Technologies" 
                  position="Software Developer Internship"
                  timeperiod="May, 2021 - Aug, 2021" 
                  :description="['Full Stack developed a component of division’s next generation product', 'Took ownership of the development cycle', 'Worked in an agile environment as a team, such as develop plans, design discussion, reviewed code, etc.', 'Technologies used: WPF, C#, XAML, SQL']" />

    <WorkTemplate companyname="Dynotify, Inc." 
                  position="Python API Developer Internship"
                  timeperiod="Feb, 2021 - May, 2021" />

  </div>

</template>

<script>
import WorkTemplate from '@/components/WorkTemplate.vue'

export default {
  name:'work',
  components: {
    WorkTemplate,
  }
}
</script>

<style scoped>

#workhistory {
  padding: 2% 20% 0 20%; 
  text-align: left;
}

</style>