<template>
  <div class="d-flex justify-content-center row body bg-light">
    <div class="col-sm-10">
      <br>
      <h1 class="text-center">Livros</h1>
      <hr><br>
      <div class="row justify-content-center">
        <button data-bs-toggle="modal" data-bs-target="#modalAddBook"
        type="button" class="btn btn-secondary btn-lg w-75">
          <i class="bi bi-bookmark-plus"></i>
          Adicionar Livro
        </button>
      </div>
      <br>
      <br>
      <Alert :message="bookStore.message" v-if="bookStore.showMessage" />
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Titulo</th>
            <th scope="col">Autor</th>
            <th scope="col">Lido?</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(book, index) in bookStore.books" :key="index">
            <td>{{ book.TITLE }}</td>
            <td>{{ book.AUTHOR }}</td>
            <td>
              <span v-if="book.READ">Sim</span>
              <span v-else>Não</span>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button @click="editBook(book)" class="btn btn-info" type="button" data-bs-toggle="modal" data-bs-target="#modalAddBook">
                  <i class="bi bi-pencil-fill"></i>
                  Editar
                </button>
                <button @click="deleteBook(book)" class="btn btn-danger" type="button" data-bs-toggle="modal" data-bs-target="#deleteModal">
                  <i class="bi bi-trash-fill"></i>
                  Deletar
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <Modal/>
  <DeleteModal/>
</template>

<script setup>
  import { onMounted } from 'vue';
  import { useBookStore } from '@/stores/books';
  import Alert from '@/components/Alert.vue';
  import Modal from '@/components/Modal.vue';
  import DeleteModal from '@/components/DeleteModal.vue';
  
  const bookStore = useBookStore()

  function editBook(book){
    bookStore.edit = true
    bookStore.editForm = book
    if (bookStore.editForm.READ == 1) {
      bookStore.editForm.READ = true
    } else {
      bookStore.editForm.READ = false
    }
  }
  
  function deleteBook(book) {
    bookStore.editForm = book
  }
  
  onMounted(() => {
    bookStore.getBooks()
  })
  </script>

<style scoped>
.body {
  min-height: 99vh;
  overflow-x:hidden;
}

</style>