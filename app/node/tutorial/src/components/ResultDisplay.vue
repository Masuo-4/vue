<script setup lang="ts">
defineProps(['features', 'survivalProbability'])

const emit = defineEmits(["displayOutput", "validateRequestValues"])

const showResult = () => emit("displayOutput")
</script>

<template>
        <button class="btn btn-primary" v-on:click="showResult()">結果を出力</button>
          <template v-if="survivalProbability !== undefined">
                    <div class="alert alert-error mt-4 ">
                      あなたの生存確率は {{ Math.round(survivalProbability) }} % です。
                    </div>
          </template>

</template>