<script setup lang="ts">
import {ref, reactive} from "vue";
import axios from "axios";
import HelloWorld from './components/HelloWorld.vue';
import ResultDisplay from './components/ResultDisplay.vue';

type typeOfFeatures = {
  Sex: '男性' | '女性' | '性別は？'
  Pclass: string
  Age: number | '年齢は？'
  Parch: number | '親・子の同伴者数は？'
  SibSp: number | '兄弟姉妹の同伴者数は？'
}

const features = reactive<typeOfFeatures>({
  Sex: '性別は？',
  Pclass: '階級は？',
  Age: '年齢は？',
  Parch: '親・子の同伴者数は？',
  SibSp: '兄弟姉妹の同伴者数は？'
})

const validateRequestValues = (): boolean => {
  if (features.Sex == '性別は？') {
    alert('性別を入力してください。')
    return false
  }
  if (features.Pclass == '階級は？') {
    alert('階級を入力してください。')
    return false
  }
  if (features.Age == '年齢は？') {
    alert('年齢を入力してください。')
    return false
  }
  if (features.Parch == '親・子の同伴者数は？') {
    alert('親子同伴者数を入力してください。')
    return false
  }
  if (features.SibSp == '兄弟姉妹の同伴者数は？') {
    alert('兄弟姉妹同伴者数を入力してください。')
    return false
  }
  // 全ての条件に引っかからなかった場合にのみ true を返す
  return true

}
const survivalProbability = ref<number | undefined>()
const displayOutput = (): void => {
  // エンドポイントを指定
  const endPoint: string = 'http://localhost:5000/api/titanic'
  // バリデーションの実行
  const validationResult: boolean = validateRequestValues()
  // バリデーションに成功していれば axios を実行
  if (validationResult === true) {
    // axios.post で POST メソッドを実行することを指示。
    // 第一引数にエンドポイント, 第二引数にリクエストボディを指定。
    axios.post(
      endPoint, features
    ).then(
      // then 以下で問題なくレスポンスが返ってきた際の挙動を記述
      (response) => {
        // TypeScriptの型指定は後ろに as をこのように付けることでも可能。
        survivalProbability.value = 100 * response.data.survival_probability as number
      }
    ).catch(
      // catch 以下では問題があった際の挙動を記述
      () => {
        alert('エラーが発生しました。')
      }
    )
  }
}



</script>

<template>
  <HelloWorld />
  <div class="container mx-auto mt-4">
      <select class="select select-primary mb-4" v-model="features.Sex">
          <option disabled selected>性別は？</option>
          <option>男性</option>
          <option>女性</option>
      </select>
      <br>
      <select class="select select-primary mb-4" v-model="features.Pclass">
          <option disabled selected>階級は？</option>
          <option>上層クラス（お金持ち）</option>
          <option>中級クラス（一般階級）</option>
          <option>下層クラス（労働階級）</option>
      </select>
      <br>
      <select class="select select-primary mb-4" v-model="features.Age">
          <option disabled selected>年齢は？</option>
          <option v-for="i in [...Array(121).keys()]">
          {{ i }}
          </option>
      </select> 歳
      <br>
      <select class="select select-primary mb-4" v-model="features.Parch">
          <option disabled selected>親・子の同伴者数は？</option>
          <option v-for="i in [...Array(11).keys()]">
          {{ i }}
          </option>
      </select> 人
      <br>
      <select class="select select-primary mb-4" v-model="features.SibSp">
          <option disabled selected>兄弟姉妹の同伴者数は？</option>
          <option v-for="i in [...Array(11).keys()]">
          {{ i }}
          </option>
      </select> 人
      <br>

  <ResultDisplay :features="features" :survivalProbability="survivalProbability" @displayOutput="displayOutput" @validateRequestValues="validateRequestValues"/>
      </div>
</template>