<template>
    <form class="login-form" @submit.prevent="login">
        <label for="user_id">USERNAME : </label>
        <input v-model="credentials.username" type="text" id="user_id"><br>
        <label for="password">PASSWORD : </label>
        <input v-model="credentials.password" type="password" name="" id="password"><br>
        <button type="submit">로그인</button>
    </form>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
    name: 'LoginForm',
    data() {
        return {
            credentials : {}
        }
    },
    methods: {
        login(){
            axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
            .then(response =>{
                console.log(response.data.token)
                const token = response.data.token
                this.$session.start()
                this.$session.set('jwt',token)
                router.push('/')
            })
            .catch(error =>{
                console.log(error)
            })
            this.credentials = []
        }
    }
}
</script>

<style>
    
</style>