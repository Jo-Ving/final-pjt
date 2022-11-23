export const backendBaseUrl = `http://127.0.0.1:8000`;
export const posterBaseUrl = `https://image.tmdb.org/t/p/original/`;

export const apiEndpoint = {
  signUp: `/accounts/signup/`,
  login: `/accounts/token/`,
  likedMovies: `/accounts/profile/`,

  movies: `/movies/`,
  movieDetail: `/movies/ID/`,
  movieReview: `/movies/ID/reviews/`,
  movieReviewCreate: `/movies/ID/reviews/`,
  movieLikeState: `/movies/ID/likes/`,

  moviePickMoie: `/movies/ID/picks/`,
};

export const movieUrl = (baseUrl, movieId) => {
  return baseUrl.replace("ID", movieId);
};
