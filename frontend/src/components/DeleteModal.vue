<template>
<div class="modal" tabindex="-1" id="deleteModal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Confirmar remoção</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Você tem certeza que deseja deletar o livro {{ editForm.TITLE }}?</p>
      </div>
      <div class="modal-footer">
        <button type="button" ref="closeModal" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
        <button @click="deleteBook" type="button" class="btn btn-danger">Confirmar</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

  export default {
    name: 'DeleteModal',
    props: {
      getBooks: Function,
      showMessage: Function,
      editForm: Object,
    },
    methods: {
      deleteBook() {
        const path = `http://localhost:5000/books/${this.editForm.ID_BOOK}`;
        axios.delete(path)
          .then((res) => {
            this.getBooks();
            this.showMessage(res.data.message);
          })
          .catch((error) => {
            console.log(error)
            this.getBooks();
          });
        this.$refs.closeModal.click();
      },
    },
  };
</script>