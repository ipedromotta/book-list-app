<template>
  <div class="modal" id="modalAddBook" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
    <div class="modal-header">
      <h5 class="modal-title" v-if="this.edit">Editar livro</h5>
      <h5 class="modal-title" v-else>Adicionar um novo livro</h5>
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
      <form @submit="onSubmit">
        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">Titulo</label>
          <input v-if="this.edit" v-model="editForm.TITLE" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o titulo">
          <input v-else v-model="addBookForm.TITLE" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o titulo">
        </div>
        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">Autor</label>
          <input v-if="this.edit" v-model="editForm.AUTHOR" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o autor">
          <input v-else v-model="addBookForm.AUTHOR" type="text" class="form-control" id="exampleFormControlInput1" required placeholder="Coloque o autor">
        </div>
        <div class="form-check">
          <input v-if="this.edit" v-model="editForm.READ" class="form-check-input" type="checkbox" id="flexCheckDefault">
          <input v-else v-model="addBookForm.READ" class="form-check-input" type="checkbox" id="flexCheckDefault">
          <label class="form-check-label" for="flexCheckDefault">
            Lido?
          </label>
        </div>
        <div class="modal-footer">
          <button @click="initForm" ref="closeModal" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
          <button type="submit" class="btn btn-primary">Salvar mudanças</button>
        </div>
      </form>
    </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: 'ModalComponent',
  data() {
    return {
      addBookForm: {
        title: '',
        author: '',
        read: []
      },
    };
  },
  props: {
    getBooks: Function,
    showMessage: Function,
    showEditModal: Function,
    edit: Boolean,
    editForm: Object
  },
  methods: {
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then((res) => {
          this.getBooks();
          this.showMessage(res.data.message);
        })
        .catch((error) => {
          console.log(error);
          this.getBooks();
        });
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then((res) => {
          this.getBooks();
          this.showMessage(res.data.message)
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.TITLE = '';
      this.addBookForm.AUTHOR = '';
      this.addBookForm.READ = undefined;
      this.showEditModal(false);
    },
    onSubmit(evt) {
      evt.preventDefault();
      let read = false;

      if (this.edit === true) {
        if (this.editForm.READ) read = true;
        const payload = {
          id: this.editForm.ID_BOOK,
          title: this.editForm.TITLE,
          author: this.editForm.AUTHOR,
          read,
        };
        this.updateBook(payload, this.editForm.id)
      } else {
        if (this.addBookForm.READ) read = true;
        const payload = {
          title: this.addBookForm.TITLE,
          author: this.addBookForm.AUTHOR,
          read, // property shorthand
        };
        console.log(payload);
        console.log(this.addBookForm);
        console.log(this.addBookForm.READ);
        this.addBook(payload);
      };
      
      this.initForm();
      this.$refs.closeModal.click();
    },
  },
};
</script>
