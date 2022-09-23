<template>
  <div class="modal" tabindex="-1" id="deleteModal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Confirmar remoção</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>Você tem certeza que deseja deletar o livro {{ bookStore.editForm.TITLE }}?</p>
        </div>
        <div class="modal-footer">
          <button type="button" ref="closeModal" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
          <button @click="bookStore.deleteBook($refs.closeModal)" type="button" class="btn btn-danger">Confirmar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBookStore } from '../stores/books';


const bookStore = useBookStore()

</script>