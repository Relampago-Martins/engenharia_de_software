//on window load
const TIME_OUT = 4000;

$(window).ready(function() {
    //load the posts
    setTimeout(function() {
        loadPosts();
    }, TIME_OUT);
});

//load posts
function loadPosts() {
    //get the posts
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: 'https://jsonplaceholder.typicode.com/posts',
        success: function(data) {
            $('#loader').hide();
            //percorre todos os posts
            $.each(data, function(index, post) {
                addPost(post);               
            });
        },
    });
}

/** 
 * Responsável por adicionar loader enquanto os comentários são carregados.
 */
function showCommentLoader(PostId){
    const commentsLoader = $('#posts-loader').clone();
    commentsLoader.removeAttr('id');
    commentsLoader.show();
    commentsLoader.attr('id', `comments-loader-${PostId}`);
    commentsLoader.appendTo(`#comments-${PostId}`);
}

/**
 * Responsável por remover o loader dos comentários.
 */
function removeCommentLoader(PostId){
    //remove from the DOM
    $(`#comments-loader-${PostId}`).remove();
}

/**
 * Responsável por adicionar um card de post na tela.
 * 
 * 1. Recebe um objeto de post.
 * 2. Duplica o card template do post .
 * 3. Adiciona os dados do post no card.
 * 4. Adiciona o card na tela removendo o atributo hidden.
 */
function addPost(post) {
    var postCard = $('#post-template').clone();
    postCard.removeAttr('id');
    postCard.removeAttr('style');
    postCard.attr('id', `post-${post.id}`);
    postCard.find('.comments-section').attr('id', `comments-${post.id}`);
    postCard.find('.comments-trigger').attr('id', `comments-trigger-${post.id}`);
    postCard.find('.card-title').text(post.title);
    postCard.find('.card-text').text(post.body);
    postCard.appendTo('#posts');
}

/** 
 * Responsável por fazer fetch dos comentários de um post.
 * e adicionar os comentários no card de post.
*/
function loadComments(buttonShowComments) {
    const postId = $(buttonShowComments).parent().attr('id').split('-')[1];
    showCommentLoader(postId);
    setTimeout(function() {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: `https://jsonplaceholder.typicode.com/posts/${postId}/comments`,
            success: function(data) {
                removeCommentLoader(postId);
                //adiciona css para esconder o botão de mostrar comentários
                $(`#comments-trigger-${postId}`).hide();
                $(`#comments-${postId}`).show();
                //percorre todos os comentários
                $.each(data, function(index, comment) {
                    addComment(postId, comment);
                });
            },
        });
    }, TIME_OUT);
}

/**
 * Percorre cada card de post e chama pega o id do post
 * e chama a função loadComments 
 */
function loadAllComments(trigger) {
    $('.comments-trigger').each(function(index, buttonShowComments) {
        loadComments(buttonShowComments);
    });
    $(trigger).hide();
}

/**
 * Responsável por adicionar um comentário no card de post.
 * 
 * 1. Recebe o id do post e um objeto de comentário.
 * 2. Duplica o card template do comentário.
 * 3. Adiciona os dados do comentário no card de post especifico.
 * 4. Adiciona o card na tela removendo o atributo hidden.
 * 
*/
function addComment(postId, comment) {
    var commentCard = $('#comment-template').clone();
    commentCard.removeAttr('id');
    commentCard.removeAttr('style');
    commentCard.attr('id', `comment-${comment.id}`);
    commentCard.text(comment.name);
    commentCard.appendTo(`#comments-${postId}`);
}

