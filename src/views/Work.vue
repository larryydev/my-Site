<template>

  <div id="workhistory" class="container">

    <h2>Work history</h2>
    <h5 style="padding: 45px 0 45px 0;">List of places that I’ve worked.</h5>

    

    <WorkTemplate companyname="Tyler Technologies" 
                  position="Software Developer Internship"
                  timeperiod="May, 2021 - Aug, 2021" 
                  :description="['Developed a component of a large-scale enterprise software desktop application using .Net C#/WPF in MVVM architecture', 'Worked with legacy code and integrated within our component', 'Took ownership of the development cycle - designing, planning, developing, and testing', 'Demoed our componenet to managers and engineers in the division']" />

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