<script setup lang="ts">
import axios from "axios";
const emit = defineEmits([""])
defineProps(['features'])


const survivalProbability = ref<number | undefined>()

const validationResult: boolean = validateRequestValues()

</script>

<template>
        <button class="btn btn-primary" v-on:click="displayOutput()">結果を出力</button>
          <template v-if="survivalProbability !== undefined">
                    <div class="alert alert-error mt-4 ">
                      あなたの生存確率は {{ Math.round(survivalProbability) }} % です。
                    </div>
          </template>

</template>