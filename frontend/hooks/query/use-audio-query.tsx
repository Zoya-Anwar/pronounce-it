import { apiClient } from "@/lib/interceptor";
import { useQuery, useQueryClient, UseQueryOptions } from "react-query";
import z from "zod";

const responseSchema = z.object({
    result: z.string(),
  });
  
  export type AudioErrorResponseData = z.infer<typeof responseSchema>;
  
  const getWord = async () => {
    const {
      data
    } = await apiClient.get<AudioErrorResponseData>("/receive_audio");
    return data;
  };
  
  type UseGetAudioQueryOptions = Omit<
    UseQueryOptions<unknown, unknown, AudioErrorResponseData>,
    "queryFn"
  >;
  
  export const useGetAudioQuery = (options?: UseGetAudioQueryOptions) => {
    const queryClient = useQueryClient();
    return useQuery({
      queryFn: getWord,
      onSuccess: (data: AudioErrorResponseData) => {},
      ...options,
      staleTime: Infinity,
    });
  };