import { useMutation, UseMutationOptions } from "react-query";
import z from "zod";

import axios, { type AxiosError } from "axios";

export const apiClient = axios.create({
  baseURL: "http://localhost:8000/api", // placeholder for backend url
  headers: {
    "Content-Type": "multipart/form-data",
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


const phonemesSchema = z.object({
  result: z.string(),
  tip: z.string(),
});

export type PhonemesData = z.infer<typeof phonemesSchema>;

const responseSchema = z.object({
  result: phonemesSchema,
});

export type AudioResponseData = z.infer<typeof responseSchema>;



const postAudio = async (audio: any) => {
  const { data } = await apiClient.post<AudioResponseData>("/audio", audio);
  return data;
};

type UsePostAudioMutationOptions = Omit<
  UseMutationOptions<AudioResponseData, unknown, unknown, unknown>,
  "mutationFn"
>;

export const usePostAudioMutation = (options?: UsePostAudioMutationOptions) => {
  return useMutation(postAudio, {
    onSuccess: () => {},
    ...options,
  });
};
