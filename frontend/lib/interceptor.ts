import axios, { type AxiosError } from "axios";

export const apiClient = axios.create({
  baseURL: "http://localhost:8080/api", // placeholder for backend url
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add a response interceptor
apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError) => {
    // if error, return error message and status code
    if (error.response) {
      return Promise.reject(error.response.data);
    }
    return Promise.reject(error);
  }
);
