import { apiClient } from "@/lib/interceptor";
import { useQuery, useQueryClient, UseQueryOptions } from "react-query";
import z from "zod";

const responseSchema = z.object({
    word: z.string(),
  });

  export type ResponseDataSentence = z.infer<typeof responseSchema>;

  const getSentence = async () => {
    const {
      data
    } = await apiClient.get<ResponseDataSentence>("/get_sentence");
    return data;
  };

  type UseGetSentenceQueryOptions = Omit<
    UseQueryOptions<unknown, unknown, ResponseDataSentence>,
    "queryFn"
  >;

  export const useGetSentenceQuery = (options?: UseGetSentenceQueryOptions) => {
    const queryClient = useQueryClient();
    return useQuery({
      queryFn: getSentence,
      onSuccess: (data: ResponseDataSentence) => {},
      ...options,
      staleTime: 1000000000000000,
    });


  };