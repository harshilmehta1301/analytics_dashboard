<template>
  <vs-table
    :max-items="descriptionItems[0]"
    pagination
    search
    :data="data"
    style="width: 100%; overflow-x: auto;"
  >
    <template #header>
        <h3>
          Logs
        </h3>
      </template>
    <template #thead>

      <vs-th
        v-for="column in columns"
        :key="column"
      >
        {{ column }}
      </vs-th>
    </template>

    <template v-slot="{data}">
      <vs-tr :key="rowIndex" v-for="(row, rowIndex) in data">
        <vs-td v-for="(column, colIndex) in keys" :key="colIndex" style="text-align: left;">
          {{ row[column] }}
        </vs-td>
      </vs-tr>
    </template>
  </vs-table>
</template>

<script>
  export default {
    name: 'AppTable',
    props: {
      table: Object
    },
    data() {
      return {
        descriptionItems: [5, 15],
        data:[],
        keys:[],
        columns:[]
      }
    },
    watch:{
      table:{
        immediate:true,
        deep:true,
         handler: function () {
          this.data = this.table['data'];
          this.keys = this.table['keys'];
          this.columns = this.table['columns'];
         }
      }
    }
  };
</script>
