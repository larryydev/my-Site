<template>

  <div id="workitem">

    <h4>{{ companyname }}</h4>
    <h6>{{ position }}</h6>
    <p>{{ timeperiod }}</p>

    <ul>
        <li v-for="item in description" :key="item.companyname">
            {{item}}
        </li>
    </ul>

  </div>

</template>

<script>
export default {
    name: "worktemplate",
    props: ['companyname', 'position', 'timeperiod', 'description']
}
</script>

<style scoped>

#workitem {
    padding: 0 0 45px 0;
}

h4 {
    padding: 0 0 5px 0;
}

h6 {
    padding: 0 0 5px 0;
}

p {
    padding: 0 0 5px 0;
}

</style>