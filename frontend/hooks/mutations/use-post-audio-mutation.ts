import { apiClient } from "@/lib/interceptor";
import { useMutation, UseMutationOptions } from "react-query";
import z from "zod";

const phonemesSchema = z.object({
  phoneme: z.string(),
  score: z.number(),
});

export type PhonemesData = z.infer<typeof phonemesSchema>;

const responseSchema = z.object({
  data: z.array(phonemesSchema),
  result: z.string(),
});

export type AudioResponseData = z.infer<typeof responseSchema>;

const requestSchema = z.object({
  audio: z.string(),
});

export type AudioRequestData = z.infer<typeof requestSchema>;

const postAudio = async (audio: AudioRequestData) => {
  const { data } = await apiClient.post<AudioResponseData>("/audio", audio);
  return data;
};

type UsePostAudioMutationOptions = Omit<
  UseMutationOptions<AudioResponseData, unknown, AudioRequestData, unknown>,
  "mutationFn"
>;

export const usePostAudioMutation = (options?: UsePostAudioMutationOptions) => {
  return useMutation(postAudio, {
    onSuccess: () => {},
    ...options,
  });
};
