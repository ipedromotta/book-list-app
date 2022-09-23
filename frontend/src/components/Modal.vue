<template>
  <div class="modal" id="modalAddBook" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" v-if="bookStore.edit">Editar livro</h5>
        <h5 class="modal-title" v-else>Adicionar um novo livro</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form @submit="bookStore.onSubmit($event, $refs.closeModal)">
          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Titulo</label>
            <input v-if="bookStore.edit" v-model="bookStore.editForm.TITLE" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o titulo">
            <input v-else v-model="bookStore.bookForm.TITLE" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o titulo">
          </div>
          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Autor</label>
            <input v-if="bookStore.edit" v-model="bookStore.editForm.AUTHOR" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o autor">
            <input v-else v-model="bookStore.bookForm.AUTHOR" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o autor">
          </div>
          <div class="form-check">
            <input v-if="bookStore.edit" v-model="bookStore.editForm.READ" class="form-check-input" type="checkbox" id="flexCheckDefault">
            <input v-else class="form-check-input" type="checkbox" id="flexCheckDefault" v-model="bookStore.bookForm.READ">
            <label class="form-check-label" for="flexCheckDefault">
              Lido?
            </label>
          </div>
          <div class="modal-footer">
            <button @click="bookStore.edit = false; bookStore.initForm()" ref="closeModal" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
            <button type="submit" class="btn btn-primary">Salvar mudanças</button>
          </div>
        </form>
      </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBookStore } from '../stores/books';


const bookStore = useBookStore()

</script>
