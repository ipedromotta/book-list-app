<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br>
        <h1>Livros</h1>
        <hr><br>
        <button data-bs-toggle="modal" data-bs-target="#modalAddBook"
        type="button" class="btn btn-success btn-sm">
          Adicionar Livro
        </button>
        <br>
        <br>
        <Alert :message="message" v-if="showMessage" />
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
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.TITLE }}</td>
              <td>{{ book.AUTHOR }}</td>
              <td>
                <span v-if="book.READ">Sim</span>
                <span v-else>Não</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button @click="editBook(book)" class="btn btn-warning" type="button" data-bs-toggle="modal" data-bs-target="#modalAddBook">Editar</button>
                  <button @click="deleteBook(book)" class="btn btn-danger" type="button" data-bs-toggle="modal" data-bs-target="#deleteModal">Deletar</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <Modal :getBooks="this.getBooks" :showMessage="this.setShowMessage" :showEditModal="this.showEditModal" :edit="this.edit" :editForm="this.editForm" />
  <DeleteModal :getBooks="this.getBooks" :editForm="this.editForm" :showMessage="this.setShowMessage" />
</template>

<script>
import axios from 'axios';
import Modal from './Modal.vue';
import Alert from './Alert.vue';
import DeleteModal from './DeleteModal.vue';

export default {
  name: 'BookComponent',
  data() {
    return {
      books: [],
      message: '',
      showMessage: false,
      edit: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.payload;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showEditModal(show) {
      this.edit = show;
    },
    editBook(book) {
      this.showEditModal(true);
      this.editForm = book;
      if (this.editForm.READ == 1) {
        this.editForm.READ = true
      } else {
        this.editForm.READ = false
      }
    },
    deleteBook(book) {
      this.editForm = book;
    },
    setShowMessage(msg) {
        this.message = msg;
        this.showMessage = true;
        setTimeout(() => {
          this.showMessage = false;
        }, 3000);
    },
  },
  created() {
    this.getBooks();
  },
  components: { Modal, Alert, DeleteModal },
};
</script>
